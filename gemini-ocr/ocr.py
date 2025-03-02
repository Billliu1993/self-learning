from google import genai
from pydantic import BaseModel


class OCR:

    def __init__(self, file_path):
        self.file_path = file_path
        self.client = genai.Client()
        self.model_id = "gemini-2.0-flash"

    def upload_file(self):

        self.pdf = self.client.files.upload(
            file=self.file_path, config={"display_name": self.file_path}
        )

    def estimate_cost(self):

        file_size = self.client.models.count_tokens(
            model=self.model_id, contents=self.pdf
        )
        print(
            f"File: {self.pdf.display_name} equals to {file_size.total_tokens} tokens"
        )

    def extract_text(self, pydantic_model: BaseModel):

        prompt = f"Extract the structured data from the following PDF file"

        response = self.client.models.generate_content(
            model=self.model_id,
            contents=[prompt, self.pdf],
            config={
                "response_mime_type": "application/json",
                "response_schema": pydantic_model,
            },
        )

        return response.parsed
