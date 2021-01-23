import { Component } from 'preact';
import { cryptm } from "../../cryptm";
import { Versions } from '../../objects/versions';

export default class Home extends Component {
	/**
	 * Constructor of the app
	 */
	constructor(){
		super();
		// The state contains the last version info
		this.state = {
			lastVersion: {
				number: null,
				date: null,
				build: null
			}
		}
	}

	/**
	 * After the component is mounted, do some actions
	 */
	componentDidMount(){
		// Replace all the email spans on the page (Javascript protection of spamming)
		cryptm("emailAlexandre","alexandre_billon", "etu", "u-bourgogne.fr");

		// Get all the soft versions to display the last
		const versions = new Versions();
		this.setState({
			lastVersion: versions.lastVersion
		});

		// Change the page title
		document.title = "FlasKlient | Accueil";
	}

	/**
	 * Render the homepage
	 * @param {Object} props The props of the homepage component
	 * @param {Object} state The state of the homepage component
	 */
	render(props, state){
		return(
			<div id="accueil" class="container-fluid">
				<div class="row">
					<div class="col-lg-12">
						<h1 class="text-center">FlasKlient !</h1>
						<p class="text-sm text-center">Logiciel mis à jour le 3 janvier 2021</p>
						<p>Bienvenue sur le logiciel de gestion de la blockchain : FlasKlient !</p>
						<p>
							Vous devez être connecté pour profiter des fonctionnalités offertes par ce logiciel. Si vous ne disposez pas d'un compte, contacter l'administrateur en écrivant un e-mail à <span class="emailAlexandre"></span> en indiquant au maximum les informations vous concernant. L'administrateur étudiera votre dossier et vous transmettra les informations nécessaires pour vous connecter. Vous pouvez également contacter par téléphone Laure OHLEYER.
						</p>
						<p class="text-center">
							<a class="btn btn-primary mr-3" href="/login">Se connecter</a>
						</p>
					</div>
				</div>

				<div class="row mt-5">
					<div class="col-lg-12">
						<h2>Informations</h2>
					</div>
					<div class="col-lg-12">
						<p>
							Ce logiciel a été développé par Alexandre BILLON et Noémie CHEVALIER, étudiants ingénieurs à l'École Supérieure d'Ingénieurs de Recherche en Matériaux et Informatique-Électronique (ESIREM) de Dijon.
						</p>
						<p>
							&copy; 2021 Alexandre BILLON, Noémie CHEVALIER. Tous droits réservés.
						</p>
						<p>
							Consulter les <a href="/mentions">mentions légales</a>.
						</p>
						<p>
							Le logiciel FlasKlient est actuellement en version <a href="/versions">{this.state.lastVersion.number}-B{this.state.lastVersion.build}</a> ({this.state.lastVersion.date }).
						</p>
					</div>
				</div>
			</div>
		);
	}
}
