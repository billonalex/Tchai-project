import { h, Component } from 'preact';
import { connect } from 'unistore/preact';
import actions from './actions';
import style from './style';

@connect('connect',actions)
export default class Login extends Component {
	state = {
		time: Date.now(),
		count: 0
	};

	// update the current time
	updateTime = () => {
		this.setState({ time: Date.now() });
	};

	increment = () => {
		this.setState({ count: this.state.count+1 });
	};

	// gets called when this route is navigated to
	componentDidMount() {
		// start a timer for the clock:
		this.timer = setInterval(this.updateTime, 1000);
		document.title = `FlasKlient | Login`;
	}

	// gets called just before navigating away from the route
	componentWillUnmount() {
		clearInterval(this.timer);
	}

	// Note: `user` comes from the URL, courtesy of our router
	render({ props }, { time, count }) {
		document.title = `FlasKlient | Login`;
		return (
			<div class={style.login}>
				<h1>Login Page !</h1>
				<p>This is the login page.</p>

				<div>Current time: {new Date(time).toLocaleString()}</div>
				<div>
					<label for="email">Enter your mail : </label>
					<input type="email" name="email"></input>
					<br></br>
					<label for="email">Enter your password : </label>
					<input type="password" name="password"></input>
				</div>
				<p>
					<button onClick={this.increment}>Click Me</button>
					{' '}
					Clicked {count} times.
				</p>
			</div>
		);
	}
}
