let start = document.getElementById("start");
let pause = document.getElementById("pause");
let listen = document.getElementById("listen");
let save = document.getElementById("save");
let exist = document.getElementById("exist");
let List

start.disabled = false;
pause.disabled = true;
listen.disabled = true;
save.disabled = true;

start.addEventListener("click", async () => {
    start.disabled = true;
    pause.disabled = false;
    listen.disabled = true;
    save.disabled = true;
    await eel.Voice_Rec_Stop("start", val);
});

pause.addEventListener("click", async () => {
    start.disabled = false;
    pause.disabled = true;
    listen.disabled = false;
    save.disabled = true;
    await eel.Voice_Rec_Stop("pause", "");
});
listen.addEventListener("click", async () => {
    start.disabled = false;
    pause.disabled = true;
    listen.disabled = true;
    save.disabled = false;
    await eel.Voice_Rec_Stop("listen", "");
});
save.addEventListener("click", async () => {
    start.disabled = false;
    pause.disabled = true;
    listen.disabled = true;
    save.disabled = true;
    await eel.Voice_Rec_Stop("save", "");
});

start.addEventListener("click", () => {
    let chrono = document.getElementById("chrono");
    let sec = 0;
    let min = 0;
    let hou = 0;
    intervalID = setInterval(() => {
        let lhou = hou < 10 ? "0" + hou : hou;
        let lmin = min < 10 ? "0" + min : min;
        let lsec = sec < 10 ? "0" + sec : sec;
        chrono.textContent = lhou + ":" + lmin + ":" + lsec;
        sec++;
        if (sec == 60) {
            sec = 0;
            min++;
        }
        if (min == 60) {
            min = 0;
            hou++;
        }
        if (hou == 24) {
            hou = 0;
            min = 0;
            sec = 0;
        }
    }, 1000);
    pause.addEventListener("click", () => {
        setTimeout(() => {
            clearInterval(intervalID);
        }, 10);
        chrono.textContent = "00:00:00";
    });
});

async function GetWav() {
    List = await eel.Exist()();
    List = List.reverse()
    console.log("line 79", List);
    let i = 0;
    if (List.length) {
        if (List.length >= 6) {
            width1 = "482px"
        }
        else {
            width1 = "500px"
        }
        List.forEach(element => {
            if (i < 15) {
                CreatElement("button", element, width1)
                i++
            }

        });

    }
};
GetWav();

function CreatElement(type, name, width) {
    let elem = document.createElement(type);
    elem.textContent = name
    elem.style.width = width
    exist.appendChild(elem);
    elem.onclick = async () => {
        console.log(`Consigne LPF/${name}.wav`);
        await eel.PlayHist(`Consigne LPF/${name}.wav`)
    }

}