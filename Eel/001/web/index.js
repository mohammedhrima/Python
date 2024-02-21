async function getDataFromPython() {
    document.getElementById("h1").innerHTML = await eel.get_data()();
}


document.getElementById("btn1").addEventListener("click", () => {
    getDataFromPython();
})

document.getElementById("btn2").addEventListener("click", async () => {
    await eel.send_data("hello from js")
})


