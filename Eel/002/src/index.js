let input = document.getElementById("result");
let buttonEnter = document.getElementById("Enter");
buttonEnter.disabled = true;

function CreatElement(type, name, id) {
    let elem = document.createElement(type);
    if (type == "button") {
        elem.className = "func"
        elem.id = id;
        let img = document.createElement("img");
        img.src = `IMG/` + name + ".png";
        elem.appendChild(img);
    }
    else if (type == "div") {
        elem.id = id
    }
    else {
        elem.innerHTML = name;
        elem.id = "chrono"
    }
    document.body.appendChild(elem);
}

function display(value) {
    if (input.value.length < 4) {
        input.value += value;
    }
    if (input.value.length == 4) {
        buttonEnter.disabled = false;
    } else {
        buttonEnter.disabled = true;
    }
}
function Clean() {
    input.value = "";
    buttonEnter.disabled = true;
}
async function Enter() {
    val = input.value;
    Clean();
    console.log("line 29 in javascript ", val);
    check = await eel.get_Matricule(val)();
    console.log("line 31 in javascript", check);
    if (check) {
        //alert("exist");
        let elem = document.getElementById("Remove");
        elem.parentNode.removeChild(elem);
        CreatElement("h1", "00:00:00", "chrono");
        CreatElement("button", "Start", "start");
        CreatElement("button", "Pause", "pause");
        CreatElement("button", "Listen", "listen");
        CreatElement("button", "Save", "save");
        CreatElement("div", "", "exist")

        var newScript = document.createElement("script");
        newScript.src = "index2.js";
        document.body.appendChild(newScript);
    } else if (!check) {
        alert("Ce matricule n'exist pas dans la base");
    }
}
