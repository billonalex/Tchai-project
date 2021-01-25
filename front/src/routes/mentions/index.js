import { Component } from 'preact';
import { cryptm } from "../../cryptm";

export default class Home extends Component {
	constructor(){
		super();
	}

	componentDidMount(){
		cryptm("email", "contact", "apgmb", "fr");
		cryptm("emailLaure","laure.ohleyer", "cote-dor", "chambagri.fr");
		cryptm("emailAlexandre","alexandre_billon", "etu", "u-bourgogne.fr");
		document.title = "FlasKlient | Mentions Légales";
	}

	render(props, state){
		document.title = "FlasKlient | Mentions Légales";
		return(
			<div class="container-fluid">
				<div class="row">
					<div class="col-lg-12">
						<h1 class="text-center">Mentions Légales</h1>
					</div>
				</div>
					
				<h3>1. Présentation du site</h3>
			</div>
		);
	}
}
