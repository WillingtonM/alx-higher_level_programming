#!/usr/bin/node
// Script that computes number of tasks completed by user id.

const request = require('request');
request(process.argv[2], function (err, resp, body) {
  if (!err) {
    const to_dos = JSON.parse(body);
    const task_comp = {};
    to_dos.forEach((todo) => {
      if (todo.completed && task_comp[todo.userId] === undefined) {
        task_comp[todo.userId] = 1;
      } else if (todo.completed) {
        task_comp[todo.userId] += 1;
      }
    });
    console.log(task_comp);
  }
});
