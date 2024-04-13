#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  list.forEach((elt) => {
    if (elt === searchElement) {
      occ++;
    }
  });

  return occ;
};
