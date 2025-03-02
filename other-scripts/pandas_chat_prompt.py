
from langchain_experimental.agents import create_pandas_dataframe_agent


'''
BASIC SETUP
@tool
def plot_chart(data: str) -> int:
    """Plots json data using plotly Figure. Use it only for ploting charts and graphs."""
    # Load JSON data
    figure_dict = json.loads(data)
    # Create Figure object from JSON data
    try:
        fig = from_json(json.dumps(figure_dict))
        st.plotly_chart(fig)
    except:
        fig = go.Figure(data)
        st.plotly_chart(fig)

tools = [plot_chart]
pandas_agent = create_pandas_dataframe_agent(llm=llm, 
                                            df=data_df, 
                                            verbose = True, 
                                            agent_type="tool-calling",
                                            allow_dangerous_code=True,
                                            max_iterations=5,
                                            return_intermediate_steps=True,
                                            extra_tools=tools
                                            )
'''

prompt = f'''
Consider the uploaded pandas data, respond intelligently to user input
You have a tool called `plot_chart` to plot charts and graphs using plotly
CHAT HISTORY: {st.session_state.history[-HISTORY_LENGTH:]}
USER INPUT: {input_text}
AI RESPONSE HERE:
'''