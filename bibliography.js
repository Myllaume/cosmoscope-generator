const fs = require("fs");
const path = require("path");

const url = "https://api.zotero.org/groups/2660172/items?format=csljson";

function genId({ author: [{ family }], issued }) {
  const year = String(issued["date-parts"][0][0]);
  return family + year;
}

fetch(url)
  .then(async (response) => {
    const data = await response.json();

    console.log(`${data.items.length} bibliographic items founded`);
    
    data.items = data.items.map((item) => {
      item.id = genId(item);
      return item;
    });
    fs.writeFile(
      path.join(__dirname, "assets", "bib.json"),
      JSON.stringify(data.items, undefined, 2),
      "utf-8",
      (err) => err && console.error("Unable to write file:", err)
    );
  })
  .catch((err) => {
    console.error("Unable to fetch:", err);
  });
