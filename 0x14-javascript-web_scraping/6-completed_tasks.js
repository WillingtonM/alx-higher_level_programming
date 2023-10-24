#!/usr/bin/node
// Script that computes number of tasks completed by user id.

const request = require('request');
request(process.argv[2], function (err, resp, body) {
  if (!err) {
    const todos = JSON.parse(body);
    const taskComp = {};
    todos.forEach((todo) => {
      if (todo.completed && taskComp[todo.userId] === undefined) {
        taskComp[todo.userId] = 1;
      } else if (todo.completed) {
        taskComp[todo.userId] += 1;
      }
    });
    console.log(taskComp);
  }
});
