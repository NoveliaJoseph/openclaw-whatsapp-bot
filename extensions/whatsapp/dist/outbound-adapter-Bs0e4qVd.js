import { t as resolveWhatsAppOutboundTarget } from "./resolve-outbound-target-BKcv4ofn.js";
import { n as normalizeWhatsAppPayloadText } from "./outbound-media-contract-zq9aNgT8.js";
import { t as createWhatsAppOutboundBase } from "./outbound-base-BgtywpNm.js";
import { shouldLogVerbose } from "openclaw/plugin-sdk/runtime-env";
import { chunkText } from "openclaw/plugin-sdk/reply-chunking";
//#region extensions/whatsapp/src/outbound-adapter.ts
let whatsAppSendModulePromise;
function loadWhatsAppSendModule() {
	whatsAppSendModulePromise ??= import("./send-DBfXQDd4.js").then((n) => n.a);
	return whatsAppSendModulePromise;
}
function normalizeOutboundText(text) {
	return normalizeWhatsAppPayloadText(text);
}
const whatsappOutbound = createWhatsAppOutboundBase({
	chunker: chunkText,
	sendMessageWhatsApp: async (to, text, options) => await (await loadWhatsAppSendModule()).sendMessageWhatsApp(to, normalizeOutboundText(text), { ...options }),
	sendPollWhatsApp: async (to, poll, options) => await (await loadWhatsAppSendModule()).sendPollWhatsApp(to, poll, options),
	shouldLogVerbose: () => shouldLogVerbose(),
	resolveTarget: ({ to, allowFrom, mode }) => resolveWhatsAppOutboundTarget({
		to,
		allowFrom,
		mode
	}),
	normalizeText: normalizeOutboundText,
	skipEmptyText: true
});
//#endregion
export { whatsappOutbound as t };
