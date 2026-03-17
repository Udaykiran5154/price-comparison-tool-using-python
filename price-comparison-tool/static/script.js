function search(){

console.log("clicked");

let product = document.getElementById("product").value;

// Loading message
document.getElementById("results").innerHTML = "🔄 Loading prices...";

fetch("/compare?product=" + product)
.then(response => response.json())
.then(data => {

console.log(data); // debug

data.sort((a, b) => {
    let p1 = parseInt(a.price.replace(/[₹,]/g, ""));
    let p2 = parseInt(b.price.replace(/[₹,]/g, ""));
    return p1 - p2;
});

let html = "";

data.forEach(item => {

html += `
<div style="border:1px solid #ccc; padding:10px; margin:10px;">
    <h3>${item.site}</h3>
    <p>Price: ${item.price}</p>
    <p>${item.best ? "⭐ Best Deal" : ""}</p>
    <a href="${item.link}" target="_blank">View Product</a>
</div>
`;

});

document.getElementById("results").innerHTML = html;

})
.catch(error => {
    console.error("Error:", error);
    document.getElementById("results").innerHTML = "❌ Failed to load data";
});

}