# `08.2` Finish delete todo

## 📝 Instructions:

Finish the `DELETE /todos/<int:position>` by completing the following steps:

1. Receive the position that the client wants to delete as the first parameter of the `delete_todo` endpoint function.

2. Remove the task from the list of `todos`, you can use any python method that allows removing items from a list by position.

3. Return the jsonify updated list of `todos`.