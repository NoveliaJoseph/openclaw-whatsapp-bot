import { t as __exportAll } from "./rolldown-runtime-CiIaOW0V.js";
import { t as resolveMergedWhatsAppAccountConfig } from "./account-config-CNQ33oav.js";
import { c as normalizeWhatsAppTarget, t as isWhatsAppGroupJid } from "./normalize-target-ePanEpfY.js";
import "./normalize-f31evwm8.js";
import { listResolvedDirectoryGroupEntriesFromMapKeys, listResolvedDirectoryUserEntriesFromAllowFrom } from "openclaw/plugin-sdk/directory-config-runtime";
//#region extensions/whatsapp/src/directory-config.ts
var directory_config_exports = /* @__PURE__ */ __exportAll({
	listWhatsAppDirectoryGroupsFromConfig: () => listWhatsAppDirectoryGroupsFromConfig,
	listWhatsAppDirectoryPeersFromConfig: () => listWhatsAppDirectoryPeersFromConfig
});
function resolveWhatsAppDirectoryAccount(cfg, accountId) {
	return resolveMergedWhatsAppAccountConfig({
		cfg,
		accountId
	});
}
async function listWhatsAppDirectoryPeersFromConfig(params) {
	return listResolvedDirectoryUserEntriesFromAllowFrom({
		...params,
		resolveAccount: resolveWhatsAppDirectoryAccount,
		resolveAllowFrom: (account) => account.allowFrom,
		normalizeId: (entry) => {
			const normalized = normalizeWhatsAppTarget(entry);
			if (!normalized || isWhatsAppGroupJid(normalized)) return null;
			return normalized;
		}
	});
}
async function listWhatsAppDirectoryGroupsFromConfig(params) {
	return listResolvedDirectoryGroupEntriesFromMapKeys({
		...params,
		resolveAccount: resolveWhatsAppDirectoryAccount,
		resolveGroups: (account) => account.groups
	});
}
//#endregion
export { listWhatsAppDirectoryGroupsFromConfig as n, listWhatsAppDirectoryPeersFromConfig as r, directory_config_exports as t };
