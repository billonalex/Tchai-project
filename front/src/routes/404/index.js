import { Component } from 'preact';

export default class NotFound404 extends Component {
	constructor(){
		super();
	}

	/**
	 * Render the 404 error page
	 */
	render(){
		document.title = "FlasKlient | 404 Error";
		return(
			<div class="container-fluid">
				<div class="row">
					<div class="col-lg-12">
						<h1 class="text-center">404 Not Found !</h1>
					</div>
				</div>
			</div>
		);
	}
}
