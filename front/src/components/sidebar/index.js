import { h, Component } from 'preact';
import { Link } from 'preact-router/match';

export default class Sidebar extends Component {
    /**
     * Close the sidebar. Triggered after a click on a sidebar button
     */
    closeSidebar() {
        document.querySelector("a.icon").click();
    }

    /**
     * Render the sidebar component
     */
    render(){
        return(
            <div id="sidebar">
                <div id="user">
                    <div class="user-img"></div>
                    <div class="user-title">FlasKlient</div>
                </div>

                <div class="sidebar-menu">
                    <div class="menu">
                        <ul>
                            <li><Link activeClassName={"active"} href="/" onClick={this.closeSidebar}>Accueil</Link></li>
                            <li><Link activeClassName={"active"} href="/profile" onClick={this.closeSidebar}>Mon Profil</Link></li>
                            <li><Link activeClassName={"active"} href="/transactions" onClick={this.closeSidebar}>Mes transactions</Link></li>
                            <li><a href="mailto:alexandre_billon@etu.u-bourgogne.fr" onClick={this.closeSidebar}>Contacter le Support</a></li>
                            <li><Link activeClassName={"active"} href="/mentions" onClick={this.closeSidebar}>Mentions Légales</Link></li>
                        </ul>
                    </div>

                    <div class="bottom">
                        <a href="/login">
                            <img src="/img/information.svg" />
                            <img src="/img/user-lock-solid.svg" />
                        </a>
                    </div>
                </div>
            </div>
        );
    }
}
