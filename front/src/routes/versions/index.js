import { Component } from 'preact';
import { Versions } from '../../objects/versions';

export default class VersionsComponent extends Component {
    /**
     * Constructor of the component
     */
    constructor() {
        super();
        this.state = {
            versions: [],
            compteurVersions: 0,
            elementsDemasques: 0
        }
    }

    /**
     * When the component is mounted, make the title pretty and get the list of the soft versions
     */
    componentDidMount(){
        document.title = "FlasKlient | Versions";
        const versions = new Versions();
        this.setState({
            versions: versions.listOfVersions
        });
    }

    /**
     * Displays more versions than already displayed in the page
     * @param {Object} state The state of the component
     */
    displayMoreVersion(state) {
        let buttonMore = document.getElementById("displaymore");
        let buttonLess = document.getElementById("displayless");
        let versionMasked = document.getElementsByClassName("masked");
        let compteur = 0;
        let limite = 5;

        if (versionMasked.length != 0) {
            while (versionMasked.length != 0 && compteur < limite) {
                state.elementsDemasques++;
                versionMasked[0].classList.remove("masked");
                buttonLess.classList.remove("masked");
                compteur++;
            }
            if (versionMasked.length == 0) {
                buttonMore.classList.add("masked");
            }
        }
        else {
            buttonMore.classList.add("masked");
        }
    }

    /**
     * Displays less versions than already displayed in the page
     * @param {Object} state The state of the component
     */
    displayLessVersion(state){
        let buttonMore = document.getElementById("displaymore");
        let buttonLess = document.getElementById("displayless");
        let version = document.querySelectorAll("div.version");
        let nbMasquees = document.querySelectorAll("div.version.masked").length + 1;
        let compteur = 0;
        let limite = 5;

        buttonMore.classList.remove("masked");

        if (state.elementsDemasques > 0) {
            while (state.elementsDemasques > 0 && compteur < limite) {
                
                if (!version[(version.length - nbMasquees - compteur)].classList.contains("masked")) {
                    version[(version.length - nbMasquees - compteur)].classList.add("masked");
                    state.elementsDemasques--;
                    compteur++;
                }
                if (state.elementsDemasques == 0) {
                    buttonMore.classList.remove("masked");
                    buttonLess.classList.add("masked");
                }
            }
        }
        else {
            state.elementsDemasques = 0;
            buttonLess.classList.add("masked");
        }
    }
    
    /**
     * Renders the component to display all the soft versions
     * @param {Object} props The props of the component
     * @param {Object} state The state of the component
     */
    render(props, state) {
        const divs = [];
        
        // For each version, create a specific div
        state.versions.forEach(version => {
            // For each item in the changelog, create a specific list item
            let items = [];
            version.items.forEach(item => {
                let itemHtml = <li><div class={`item item-${item.type.toLowerCase()}`}>{ item.type }</div>{ item.content }</li>
                items.push(itemHtml);
            });

            let div = <div class={ 'card version ' + (state.compteurVersions > 4 ? 'masked' : '') }>
                    <h4><div id="number">{ version.number }</div>{ version.date }</h4>
                    <p id="item">
                        <ul>
                            { items }
                        </ul>
                    </p>
                </div>
            divs.push(div);
            state.compteurVersions++;
        });

        return (
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12">
                        <h1>Historique des versions</h1>
                        { divs }
                        {(state.compteurVersions > 5) && (
                            <div>
                                <button id="displaymore" onClick={() => this.displayMoreVersion(this.state)} class="btn btn-primary"><i class="fas fa-chevron-down"></i> &nbsp; Afficher plus</button> &nbsp; &nbsp;
                                <button id="displayless" onClick={() => this.displayLessVersion(this.state)} class="btn btn-primary masked"><i class="fas fa-chevron-up"></i> &nbsp; Afficher moins</button>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        );
    }
}
