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
				<p>Conformément aux dispositions des articles 6-III et 19 de la Loi n° 2004-575 du 21 juin 2004 pour la Confiance dans l'économie numérique, dite L.C.E.N., nous portons à la connaissance des utilisateurs et visiteurs du site : <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> les informations suivantes :</p>

				<p><strong>Informations légales</strong></p>

				<p>Nom de l'organisme : <strong>APGMB</strong><br />
				Adresse : <strong>1, Rue des Coulots - 21110 BRETENIÈRE</strong><br />
				Téléphone : <strong>03 80 68 66 77</strong><br />
				SIRET : <strong>815 243 282 00028</strong> immatriculée au R.C.S. de <strong>Dijon</strong><br />
				APE : <strong>9499Z</strong> Autres organisations fonctionnant par adhésion volontaire<br />
				Numéro de TVA intercommunautaire : <strong>FR 85 815243282</strong><br />
				Adresse de courrier électronique : <strong><span class="email"></span></strong> <br />
					<br />
				Le Créateur du site est : <strong>Nicolas TOURRETTE</strong>, <strong>Alexandre BILLON</strong><br />
				Le Responsable de la  publication est : <strong>Laure OHLEYER</strong><br />
				Contactez le responsable de la publication : <strong><span class="emailLaure"></span></strong><br />
				<br />
				Le Webmaster est : <strong>Nicolas TOURRETTE / Alexandre BILLON</strong><br />
				Contactez le Webmaster : <strong><a href="http://support.apgmb.fr" target="_blank">site du Support technique</a></strong><br />
				L'hébergeur du site est : <strong>OVH.com - 2, Rue Kellermann - 59100 Roubaix</strong><br />
				<span style="font-size: 40%;"><strong>CREDITS :</strong> les mentions légales ont étés générées par <strong><a href="https://www.generer-mentions-legales.com">ce site</a></strong>.</span></p>
					
				<h3>2. Description des services fournis</h3>

				<p>Le site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> a pour objet de fournir la gestion documentaire de la filière moutarde gérée par l'APGMB.<br />
				Le propriétaire du site s’efforce de fournir sur le site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> des informations aussi précises que possible. Toutefois, il ne pourra être tenue responsable des omissions, des inexactitudes et des carences dans la mise à jour, qu’elles soient de son fait ou du fait des tiers partenaires qui lui fournissent ces informations.<br />
				Tous les informations proposées sur le site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> sont données à titre indicatif, sont non exhaustives, et sont susceptibles d’évoluer. Elles sont données sous réserve de modifications ayant été apportées depuis leur mise en ligne.<br />
				</p>

				<h3>3. Propriété intellectuelle et contrefaçons</h3>

				<p>
				Le propriétaire du site est propriétaire des droits de propriété intellectuelle ou détient les droits d’usage sur tous les éléments accessibles sur le site, notamment les textes, images, graphismes, logo, icônes, sons, logiciels…<br />
				Toute reproduction, représentation, modification, publication, adaptation totale ou partielle des éléments du site, quel que soit le moyen ou le procédé utilisé, est interdite, sauf autorisation écrite préalable à l 'email : <strong><span class="email"></span></strong>.<br />
				Toute exploitation non autorisée du site ou de l’un des éléments qu’il contient sera considérée comme constitutive d’une contrefaçon et poursuivie conformément aux dispositions des articles L.335-2 et suivants du Code de Propriété Intellectuelle.
				</p>

				<h3>4. Liens hypertextes et cookies</h3>

				<p>Le site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> contient un certain nombre de liens hypertextes vers d’autres sites (partenaires, informations…) mis en place avec l’autorisation du propriétaire du site. Cependant, le propriétaire du site n’a pas la possibilité de vérifier le contenu des sites ainsi visités  et décline donc toute responsabilité de ce fait quant aux risques éventuels de contenus illicites.<br />
				<br />
				L’utilisateur est informé que lors de ses visites sur le site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a>, un ou des cookies sont susceptible de s’installer automatiquement sur son ordinateur. Un cookie est un fichier de petite taille, qui ne permet pas l’identification de l’utilisateur, mais qui enregistre des informations relatives à la navigation d’un ordinateur sur un site. Les données ainsi obtenues visent à faciliter la navigation ultérieure sur le site, et ont également vocation à permettre diverses mesures de fréquentation.<br />
				<br />
				Le paramétrage du logiciel de navigation permet d’informer de la présence de cookies et éventuellement, de refuser de la manière décrite à l’adresse suivante : <a href="https://www.cnil.fr" target="_blank">www.cnil.fr</a>.<br />
				Le refus d’installation d’un cookie peut entraîner l’impossibilité d’accéder à certains services. L’utilisateur peut toutefois configurer son ordinateur de la manière suivante, pour refuser l’installation des cookies :<br />
				Sous Internet Explorer : onglet outil / options internet. Cliquez sur Confidentialité et choisissez Bloquer tous les cookies. Validez sur OK.
				</p>

				<h3>5. Protection des biens et des personnes - Gestion des données personnelles</h3>

				<p>Utilisateur : Internaute se connectant, utilisant le site susnommé : <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a>.<br />
				En France, les données personnelles sont notamment protégées par la loi n° 78-87 du 6 janvier 1978, la loi n° 2004-801 du 6 août 2004, l'article L. 226-13 du Code pénal et la Directive Européenne du 24 octobre 1995.</p>

				<p>Sur le site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a>, le propriétaire du site ne collecte des informations personnelles relatives à l'utilisateur que pour le besoin de certains services proposés par le site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a>. L'utilisateur fournit ces informations en toute connaissance de cause, notamment lorsqu'il procède par lui-même à leur saisie. Il est alors précisé à l'utilisateur du site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> l’obligation ou non de fournir ces informations.<br />
				Conformément aux dispositions des articles 38 et suivants de la loi 78-17 du 6 janvier 1978 relative à l’informatique, aux fichiers et aux libertés, tout utilisateur dispose d’un droit d’accès, de rectification, de suppression et d’opposition aux données personnelles le concernant. Pour l’exercer, adressez votre demande à <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> par email : email du webmaster ou  en effectuant sa demande écrite et signée, accompagnée d’une copie du titre d’identité avec signature du titulaire de la pièce, en précisant l’adresse à laquelle la réponse doit être envoyée.</p>

				<p>Aucune information personnelle de l'utilisateur du site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> n'est publiée à l'insu de l'utilisateur, échangée, transférée, cédée ou vendue sur un support quelconque à des tiers. Seule l'hypothèse du rachat du site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> à le propriétaire du site et de ses droits permettrait la transmission des dites informations à l'éventuel acquéreur qui serait à son tour tenu de la même obligation de conservation et de modification des données vis à vis de l'utilisateur du site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a>.</p>

				<p>Le site <a href="https://qualim.apgmb.fr" target="_blank">https://qualim.apgmb.fr</a> est en conformité avec le RGPD.</p>

				<p>Les bases de données sont protégées par les dispositions de la loi du 1<sup>er</sup> juillet 1998 transposant la directive 96/9 du 11 mars 1996 relative à la protection juridique des bases de données.</p>

			</div>
		);
	}
}
