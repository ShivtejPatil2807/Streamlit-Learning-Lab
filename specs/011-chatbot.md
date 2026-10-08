# 011: Chatbot project

**Files:** `pages/22_Project_Chatbot.py`, `core/lessons.py`
**Status:** Implemented

## Purpose
The third mini project: a chatbot that remembers the conversation. It answers
with simple keyword rules, so it needs no AI model, no account and no key, and
it is safe to run on a public site. The last part shows, as code only, how to
swap in a real language model.

## Requirements
- **R1** The project is listed in the registry in the category "Projects".
- **R2** The page has five numbered parts: the idea, three steps (what the bot
  knows, find the answer, remember the conversation) and "Using a real
  language model". Each step has the Learn, Code and Try tabs.
- **R3** "What the bot knows" lists every keyword group with its answer.
- **R4** "Find the answer" starts with a chart question and shows the chart
  answer. A question about caching shows the caching answer. A question the bot
  does not know shows "I do not know that one yet."
- **R5** The chat starts with one greeting from the assistant.
- **R6** Asking a question adds the question and the bot's answer, so the chat
  then has three messages, in the order assistant, user, assistant.
- **R7** The conversation is remembered: after the page reruns, the messages
  are still there and are not duplicated.
- **R8** A question the bot does not know gets "I do not know that one yet."
  in the chat.
- **R9** The downloaded script runs on its own and keeps the knowledge
  function (without its decorator). The real-model code stays as text and does
  not add a package to the `pip install` line.

## Notes
- The matching is word by word: lower-case, strip punctuation, remove a final
  "s", then compare with the keywords. It is simple on purpose.
- The real-model example never contains a key. A public app must not hold the
  owner's key, because every visitor would spend the owner's credit.
