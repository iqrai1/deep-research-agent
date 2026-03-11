import os
from typing import Dict

import resend
from agents import Agent, function_tool


@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body"""
    resend.api_key = os.environ.get("RESEND_API_KEY")
    
    response = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": ["iqrajannat88@gmail.com"],
        "subject": subject,
        "html": html_body
    })
    
    print("Email response", response["id"])
    return "success"

INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)
