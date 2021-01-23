import { h, Component } from 'preact';
/*import { Link } from 'preact-router/match';
import style from './style.css';

const Header = () => (
	<header class={style.header}>
		<h1>Preact App</h1>
		<nav>
			<Link activeClassName={style.active} href="/">Home</Link>
			<Link activeClassName={style.active} href="/profile">Me</Link>
			<Link activeClassName={style.active} href="/profile/john">John</Link>
		</nav>
	</header>
);

export default Header;
*/

export default class TopNavbar extends Component {

	/**
	 * Construct the top navbar
	 * @param {Object} props 
	 */
	constructor(props){
		super(props);
		this.state = {
			active: null
		}
	}

	/**
	 * While component is mounted, add a class to the div#page to adjust its size
	 */
	componentDidUpdate(){
		if (this.props.items.length > 0) {
			document.getElementById("page").classList.add("navtop-sm");
			this.props.items.forEach(item => {
				if(item[1] === this.props.url){
					document.querySelectorAll("a.nav-link").forEach(item => {
						item.classList.remove("activated");
					});
					document.querySelector(`a.nav-link[href='${this.props.url}']`).classList.add("activated");
				}
			});
		}
		else {
			document.getElementById("page").classList.remove("navtop-sm");
		}
	}

	/**
	 * Change the active element of the navbar
	 */
	setActive = (element) => {
		this.setState({
			active: element[0]
		});
	}

	/**
	 * Render the component
	 * @param {Object} props The component props property
	 * @param {Object} state The component state property
	 */
	render(props, state) {
		if(props.items.length > 0){
			let items = props.items.map(item => (
				<a class={"nav-link" + (state.active == item[0] ? " activated" : "")} onClick={() => this.setActive(item)} href={item[1]}>{item[0]}</a>
			));
			return (
				<div id="nav-top-container">
					<div class="nav-scroller bg-white shadow-sm">
						<nav id="nav-top" class="nav nav-underline">
							{ items }
						</nav>
					</div>
				</div>
			);
		}
	}
}