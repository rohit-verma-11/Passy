function Activate(section){
    document.getElementById('passwords').style.display = "none";
    document.getElementById('profile').style.display = "none";
    document.getElementById(section).style.display = "flex";
    document.getElementById('top').innerHTML = `<h1>${section.charAt(0).toUpperCase() + section.slice(1)}</h1>`;
    document.getElementById('top').style.color = "#c5c6c7";
}