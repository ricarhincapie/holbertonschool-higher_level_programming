#!/usr/bin/node
exports.addMeMaybe = function (x, theFunction) {
  theFunction(x = x + 1);
};
