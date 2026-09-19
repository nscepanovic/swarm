// Minimalan markdown -> HTML za nase fajlove (context/agents.md).
// Sve se prvo escape-uje, pa tek onda se dodaju nasi tagovi: sadrzaj fajla
// nikad ne moze da ubaci svoj HTML u stranicu.
const esc = (s: string) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

const inline = (s: string) =>
  esc(s)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");

export function renderMarkdown(md: string): string {
  const out: string[] = [];
  const lines = md.split("\n");
  let para: string[] = [];
  let list: string[] = [];
  const flushPara = () => { if (para.length) out.push(`<p>${inline(para.join(" "))}</p>`); para = []; };
  const flushList = () => { if (list.length) out.push(`<ul>${list.map((l) => `<li>${inline(l)}</li>`).join("")}</ul>`); list = []; };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.startsWith("```")) {
      flushPara(); flushList();
      const code: string[] = [];
      while (++i < lines.length && !lines[i].startsWith("```")) code.push(lines[i]);
      out.push(`<pre><code>${esc(code.join("\n"))}</code></pre>`);
    } else if (/^#{1,4} /.test(line)) {
      flushPara(); flushList();
      const level = Math.min(line.indexOf(" ") + 1, 4);
      out.push(`<h${level}>${inline(line.slice(line.indexOf(" ") + 1))}</h${level}>`);
    } else if (/^\s*- /.test(line)) {
      flushPara();
      list.push(line.replace(/^\s*- /, ""));
    } else if (/^\s{2,}\S/.test(line) && list.length) {
      list[list.length - 1] += " " + line.trim();
    } else if (!line.trim()) {
      flushPara(); flushList();
    } else {
      flushList();
      para.push(line.trim());
    }
  }
  flushPara(); flushList();
  return out.join("\n");
}
