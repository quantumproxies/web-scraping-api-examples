// Web page to Markdown: one POST /v1/scrape.
//
//   export QUANTICDATA_API_KEY=...        # https://app.quanticdata.io/register
//   node markdown.mjs https://www.iana.org/help/example-domains
//
// Node 18+, no dependencies.
// Docs: https://quanticdata.io/docs/#scrape

const KEY = process.env.QUANTICDATA_API_KEY;
if (!KEY) {
  console.error("Set QUANTICDATA_API_KEY first: https://app.quanticdata.io/register");
  process.exit(1);
}
const [url = "https://www.iana.org/help/example-domains"] = process.argv.slice(2);

const res = await fetch("https://api.quanticdata.io/v1/scrape", {
  method: "POST",
  headers: { Authorization: `Bearer ${KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({ url, format: "markdown" }),
});
const body = await res.json();
if (!res.ok || body.type === "error") {
  console.error(`Request failed (${res.status}): ${body.message}`);
  process.exit(1);
}
const { payload } = body;

console.error(`# ${payload.title} (${payload.status}, ${payload.content.length} chars)`);
console.log(payload.content);
