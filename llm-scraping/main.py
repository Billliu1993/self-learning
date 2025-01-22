import os
import asyncio
import json
from pydantic import BaseModel, Field
from typing import List, Literal
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import LLMExtractionStrategy

URL_TO_CRAWL = ""

LLM_INSTRUCTION = """
Exract the following information from the company profile page:
- companyName: The name of the company
- companyDescription: A brief description of the company
- currentJobOpenings: A list of current job titles openings at the company
- travelingDemand: Estimated travel demand for the company based on the job listings and company description. This field can only have one of the following values: 'low', 'median', 'high'
- travelingDemandReason: Reason for why you choose the estimated travel demand for the company based on the job listings and company description
"""


class CompanyProfile(BaseModel):
    companyName: str = Field(description="The name of the company")
    companyDescription: str = Field(description="A brief description of the company")
    currentJobOpenings: List[str] = Field(
        description="A list of current job titles openings at the company"
    )
    travelingDemand: Literal["low", "median", "high"] = Field(
        description="Estimated travel demand for the company based on the job listings and company description"
    )
    travelingDemandReason: str = Field(
        description="Reason for why you choose the estimated travel demand for the company based on the job listings and company description"
    )


async def main():
    # 1. Define the LLM extraction strategy
    llm_strategy = LLMExtractionStrategy(
        provider="openai/gpt-4o-mini", # or "deepseek/deepseek-chat"
        api_token=os.getenv("OPENAI_API_KEY"), # or "DEEPSEEK_API_KEY"
        schema=CompanyProfile.model_json_schema(),
        extraction_type="schema",
        instruction=LLM_INSTRUCTION,
        chunk_token_threshold=1000,
        overlap_rate=0.0,
        apply_chunking=True,
        input_format="markdown",
        extra_args={"temperature": 0.2, "max_tokens": 800},
    )

    # 2. Build the crawler config
    crawl_config = CrawlerRunConfig(
        extraction_strategy=llm_strategy,
        cache_mode=CacheMode.BYPASS,
        process_iframes=False,
        remove_overlay_elements=True,
        exclude_external_links=True,
    )

    # 3. Create a browser config if needed
    browser_cfg = BrowserConfig(headless=True, verbose=True)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        # 4. Let's say we want to crawl a single page
        result = await crawler.arun(url=URL_TO_CRAWL, config=crawl_config)

        if result.success:
            # 5. The extracted content is presumably JSON
            data = json.loads(result.extracted_content)
            print("Extracted items:", data)

            # 6. Show usage stats
            llm_strategy.show_usage()  # prints token usage
        else:
            print("Error:", result.error_message)


if __name__ == "__main__":
    asyncio.run(main())
