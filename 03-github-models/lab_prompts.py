import json

prompts = {
    "SYSTEM": """
    You are a support assistant.
    Given a customer support ticket, respond only with a JSON object containing two keys:
    * category: one of [Billing, Technical Issue, Feature Request, Other]
    * summary: a one-sentence summary of the issue.
    """,
    "USER": """
    Example ticket:
    Hi team,
    Since the 2.3.1 update, whenever I try to upload a file larger than 5 MB, the process failed with an "Unknown Error".
    I've tried multiple files and network connections but get the same result.
    Thanks,
    -Taylor
    """,
    "ASSISTANT": json.dumps(
        {
            "category": "Technical Issue",
            "summary": "File uploads over 5 MB fail with and 'Unknown Error' after the 2.3.1 update.",
        }
    ),
    "SAMPLES": [
        """
    Hi there,
    Last week I upgraded to the Pro plan but I was charged twice.
    Can someone please reverse the extra charge?
    Thanks,
    Jordan
    """,
        """
    Hi team,
    Since the 2.3.1 update, whenever I try to upload a file larger than 5 MB, the process fails with an 'Unknown Error.' 
    I've tried multiple files and network connections but get the same result.
    Thanks,
    Taylor
    """,
        """
    Hello,
    I love the new dashboard, but it would be extremely helpful if I could export the report charts as CSV or Excel files directly, instead of manually copying data.
    Best,
    -Morgan
    """,
        """
    Hey there,
    I'm trying to find your API rate limits but can't see them anywhere in the documentation. 
    Could you point me to the right place?
    Cheers,
    Casey
    """,
    ],
}
