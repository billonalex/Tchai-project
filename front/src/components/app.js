import { h, Component } from 'preact';
import { Router, Route } from 'preact-router';

import Header from './topnavbar';
import TopNavbar from './topnavbar';
import Sidebar from './sidebar';
import Footer from './footer';

// Code-splitting is automated for routes
import Home from '../routes/home';
import Profile from '../routes/profile';
import VersionsComponent from '../routes/versions';
import MentionsLegales from '../routes/mentions';
import NotFound404 from '../routes/404';
import Login from '../routes/login';

export default class App extends Component {

	constructor(){
		super();
		this.state = {
			navbar: {
				items: [],
				url: null
			}
		};
	}
	
	/** Gets fired when the route changes.
	 *	@param {Object} event		"change" event from [preact-router](http://git.io/preact-router)
	 *	@param {string} event.url	The newly routed URL
	 */
	handleRoute = event => {
		this.currentUrl = event.url;
		this.displayTopNavbar();
	};

	/**
	 * Displays the top navbar depending of the page URL
	 */
	displayTopNavbar(){
		let itemsToAdd = [];

		switch (this.currentUrl) {
			case "/":
				itemsToAdd = [["Accueil", "/"], ["Mon Profil", "/profile"], ["John", "/profile/John"]];
				break;
			case "/profile/John":
				itemsToAdd = [["Accueil 2", "/"], ["IGP 2", "/igp"], ["John 2", "/profile/John"]];
				break;
			default:
				this.reinitTopNavbar();
				break;
		}

		this.setState({
			navbar: {
				items: itemsToAdd,
				url: this.currentUrl
			}
		});
	}

	/**
	 * Reinit the top navbar
	 */
	reinitTopNavbar(){
		this.setState({
			navbar: {
				items: [],
				url: null
			}
		});
	}

	/**
	 * Before the component will be mounted, load the Font Awsome script
	 */
	componentWillMount(){
		const script = document.createElement("script");
		script.src = "https://kit.fontawesome.com/eaee607de4.js";
		script.async = true;
		document.head.appendChild(script);
	}

	/**
	 * The component is mounted, adds actions to make the sidebar working on mobile devices
	 */
	componentDidMount(){
		document.querySelector("a.icon").addEventListener("click", () => {
			if (!document.getElementById("sidebar").classList.contains("responsive")) {
				document.querySelector("a.icon").innerHTML = '<i class="far fa-times-circle"></i>';
			}
			else {
				document.querySelector("a.icon").innerHTML = '<i class="fas fa-bars"></i>';
			}
			document.querySelector("a.icon").classList.toggle("text-light");
			document.getElementById("sidebar").classList.toggle("responsive");
			document.querySelector(".sidebar-menu").classList.toggle("responsive");
		});
	}

	/**
	 * Render the app
	 */
	render() {
		return (
			<div id="app">
				<a class="icon">
					<i class="fas fa-bars"></i>
				</a>

				<Sidebar />
				<div id="content">
					<TopNavbar items={this.state.navbar.items} url={this.state.navbar.url} />
					<div id="page">
						<Router onChange={this.handleRoute}>
								<Home path="/" />
								<Profile path="/profile/" user="me" />
								<Profile path="/profile/:user" />
								<Login path="/login" />
								<VersionsComponent path="/versions" />
								<MentionsLegales path="/mentions" />
								<NotFound404 path="/*" />
								<Route path="/*" Component={NotFound404} />
						</Router>
					</div>
					<Footer />
				</div>
			</div>
		);
	}
}
