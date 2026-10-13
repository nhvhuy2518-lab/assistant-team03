\# AI Service Interface



\## 1. Purpose



This document defines the interface for a future Large Language Model (LLM) service used by the university assistant. No actual LLM call is implemented at this stage.



\## 2. Function Signature



```python

def generate\_answer(question: str, context: str = "") -> AIResponse:

&#x20;   pass

```



\## 3. Inputs



| Parameter | Type | Description |

|---|---|---|

| question | str | The user's question. Must not be empty. |

| context | str | Optional relevant information retrieved from university documents. |



\## 4. Outputs



The function returns an `AIResponse` object.



| Field | Type | Description |

|---|---|---|

| answer | str | The generated answer. |

| success | bool | Indicates whether answer generation succeeded. |

| error | str or None | Error information when generation fails. |



\## 5. Errors



The service should handle the following cases:



\- Empty question: reject the input.

\- Invalid input: return an appropriate error.

\- LLM service unavailable: report the failure.

\- Request timeout: stop waiting and report a timeout.

\- Empty model response: report that no answer was generated.



\## 6. Fallback Strategy



If the LLM service fails, the assistant should:



1\. Search available university data for a direct answer.

2\. Return verified information if a suitable result is found.

3\. If no reliable information is available, explain that the answer is unavailable and direct the user to the appropriate university office.



The system must not invent university policies, deadlines, or contact details.



\## 7. Current Implementation Status



This document defines the planned interface only. No actual LLM API call, API key, or model integration is required at this stage.

