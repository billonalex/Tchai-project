export function cryptm(className, m, o, n) {
    for (let i = 0; i < document.getElementsByClassName(className).length; ++i) {
        let email = document.createElement("a");
        email.setAttribute("href", 'mailto:' + m + '@' + o + '.' + n);
        email.setAttribute("style", "text-decoration: none;");
        email.innerHTML = m + '@' + o + '.' + n + ' <img src="/img/security.svg" width="14" height="14">';

        document.getElementsByClassName(className)[i].innerHTML = "";
        document.getElementsByClassName(className)[i].appendChild(email);
    }
}