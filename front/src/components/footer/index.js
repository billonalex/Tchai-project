import { h, Component } from 'preact';
import { Versions } from '../../objects/versions';

export default class Footer extends Component {

	/**
	 * While the component is mounted, display the last version of the software in the footer.
	 */
	componentDidMount(){
		const versions = new Versions();
		const lastVersion = versions.lastVersion;
		document.getElementById("foot-version").innerHTML = lastVersion.number + ' (build ' + lastVersion.build + ')';
		document.getElementById("foot-version-release").innerHTML = lastVersion.date;
	}

	/**
	 * Render the component
	 */
	render(){
		return(
			<div id="footer">
				<div class="row text-sm">
					<div class="col">
						<p>&copy; 2020 Alexandre BILLON - Noémie CHEVALIER. Tous droits réservés.</p>
					</div>
					<div class="col float-right text-right">
						<a href="/versions"><p>Version <span id="foot-version"></span></p></a>
						<p>Release <span id="foot-version-release"></span></p>
					</div>
				</div>
			</div>
		);
	}
}
