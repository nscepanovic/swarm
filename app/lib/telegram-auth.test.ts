import assert from "node:assert/strict";
import { verifyInitData, signInitData } from "./telegram-auth.ts";

const TOKEN = "123456:TEST-token";
const now = String(Math.floor(Date.now() / 1000));
const user = JSON.stringify({ id: 316068566, first_name: "Nemanja" });

const good = signInitData({ auth_date: now, query_id: "AAH", user }, TOKEN);
assert.equal(verifyInitData(good, TOKEN)?.id, 316068566, "ispravan potpis prolazi");

assert.equal(verifyInitData(good, "999:drugi-token"), null, "tudji token ne prolazi");

const tampered = good.replace("316068566", "111111111");
assert.equal(verifyInitData(tampered, TOKEN), null, "izmenjen korisnik ne prolazi");

const old = signInitData({ auth_date: String(Number(now) - 2 * 86400), user }, TOKEN);
assert.equal(verifyInitData(old, TOKEN), null, "stariji od 24h ne prolazi");

const withSig = signInitData({ auth_date: now, user, signature: "abc" }, TOKEN);
assert.equal(verifyInitData(withSig, TOKEN)?.id, 316068566, "radi i sa signature poljem");

assert.equal(verifyInitData("", TOKEN), null, "prazno ne prolazi");
assert.equal(verifyInitData("user=x&hash=zz", TOKEN), null, "los hash ne prolazi");

console.log("telegram-auth: svih 7 provera prolazi");
