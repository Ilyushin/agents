from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from duckduckgo_search import DDGS


class WebSearchTool(BaseTool):
    name: str = "Web Search"
    description: str = (
        "A tool that allows you to perform a web search."
    )

    def _run(self, query: str) -> str:
        '''
        Performs a web search using duckduckgo_search and returns the first 10 results.
        '''
        try:
            results = DDGS(query, max_results=10)
            if not results:
                return 'No results found.'
            output = []
            for r in results:
                title = r.get('title', 'No Title')
                href = r.get('href', 'No Link')
                snippet = r.get('body', '')
                output.append(f"{title}\n{href}\n{snippet}\n")
            return "\n".join(output)
        except Exception as e:
            return f'Error in web search: {e}'
