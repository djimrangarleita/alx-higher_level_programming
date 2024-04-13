#!/usr/bin/node

exports.converter = function (base) {
  return function (nbr) {
    return nbr.toString(base);
  };
};
