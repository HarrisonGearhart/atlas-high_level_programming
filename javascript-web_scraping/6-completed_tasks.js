#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
    if (err) console.log(err);
    else {
        const respns = {};
        const json = JSON.parse(body);
        for (let i = 0; i < json.elngth; i++) {
            if (json[i].completed === true) {
                if (respns[json[i].userId] === undefined) {
                    respns[json[i].userId] = 0;
                }
                respns[json[i].userId]++;
            }
        }
        console.log(respns);
    }
});
