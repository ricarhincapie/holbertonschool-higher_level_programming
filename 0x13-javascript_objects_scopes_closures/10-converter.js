#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    const res = number.toString(base);
    return res;
  };
};
