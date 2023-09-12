#!/usr/bin/node

exports.esrever = function (list) {
  const rlist = [];
  for (let x = list.length - 1; x >= 0; x--) {
    rlist.push(list[x]);
  }

  return (rlist);
};

