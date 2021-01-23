/**
 * A class which contains all the software versions.
 */
export class Versions {
    listOfVersions = [];
    lastVersion = {};

    /**
     * Constructor of the Versions object
     */
    constructor(){
        this.listOfVersions = [
            {
                number: "undefined",
                date: "undefined",
                build: "undefined"
            }
        ];
        
        this.lastVersion = this.listOfVersions[0];
        this.getVersions();
    }

    /**
     * Get the list of version from the /front/config/versions.json file
     */
    getVersions(){
        this.listOfVersions = require("../config/versions.json");
        this.lastVersion = this.listOfVersions[0];
    }
}