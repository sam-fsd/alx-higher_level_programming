#!/usr/bin/node
//  a script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const allTasks = JSON.parse(body);
    const doneTasks = {};

    for (let i = 0; i < allTasks.length; i++) {
      const userId = allTasks[i].userId;
      let userTasks = 0;
      for (let j = 0; j < allTasks.length; j++) {
        const userData = allTasks[j];
        if (userId === userData.userId) {
          if (userData.completed === true) userTasks++;
        }
      }
      doneTasks[`${userId}`] = userTasks;
    }
    console.log(doneTasks);
  }
});
