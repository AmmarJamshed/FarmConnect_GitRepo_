// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CowIdentity {
    struct Cow {
        string breed;
        uint age;
        address owner;
    }

    mapping(string => Cow) public cows;

    function registerCow(string memory id, string memory breed, uint age, address owner) public {
        cows[id] = Cow(breed, age, owner);
    }

    function getCow(string memory id) public view returns (string memory, uint, address) {
        Cow memory cow = cows[id];
        return (cow.breed, cow.age, cow.owner);
    }
}