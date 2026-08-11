# Plan de a una / One Thing at a Time

[![Validate skill](https://github.com/santijnolan/codex-one-thing-at-a-time/actions/workflows/validate.yml/badge.svg)](https://github.com/santijnolan/codex-one-thing-at-a-time/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Una skill abierta para OpenAI Codex que transforma planes complejos en una conversación liviana: una decisión importante por vez durante la planificación y ejecución autónoma de todo lo aprobado cuando el plan queda cerrado.

Está pensada para reducir carga cognitiva y conservar control sobre las decisiones. Puede ser especialmente útil para personas con TDAH, sin convertir el trabajo en una lista interminable de confirmaciones.

## Cómo funciona

1. Codex investiga el estado real antes de proponer cambios.
2. Presenta una sola decisión con problema, cambio, consecuencias, riesgo y recomendación.
3. La persona puede aprobarla, ajustarla o descartarla.
4. La planificación continúa de a una decisión y queda registrada.
5. Durante esta etapa no se implementa nada.
6. Al cerrar el plan, Codex ejecuta y verifica todo lo aprobado sin volver a pedir permiso por cada acción técnica.

## Instalación

### Desde Codex

Pedile a Codex:

```text
Instalá la skill desde https://github.com/santijnolan/codex-one-thing-at-a-time/tree/main/skills/one-thing-at-a-time
```

O usá el instalador incluido en Codex:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo santijnolan/codex-one-thing-at-a-time \
  --path skills/one-thing-at-a-time
```

La skill estará disponible en el siguiente turno de Codex.

### Instalación manual

```bash
git clone https://github.com/santijnolan/codex-one-thing-at-a-time.git
mkdir -p ~/.codex/skills
cp -R codex-one-thing-at-a-time/skills/one-thing-at-a-time ~/.codex/skills/
```

## Uso

```text
Usá $one-thing-at-a-time para que acordemos el plan una decisión por vez y después ejecutes todo lo aprobado.
```

También puede activarse con frases naturales como “armemos el plan de a una”, “quiero aprobar cada decisión” o “no me muestres todo junto”.

## Contribuir

Issues y pull requests son bienvenidos. Leé [CONTRIBUTING.md](CONTRIBUTING.md) antes de proponer cambios. El CI valida el formato de la skill y evita que se incorporen rutas o referencias privadas por accidente.

## English

An open-source OpenAI Codex skill for cognitively lighter planning: Codex researches first, presents one meaningful plan decision at a time, records explicit approvals, and only after the plan is complete executes and verifies all approved work autonomously.

Install it by asking Codex to install the skill from the GitHub URL above, or run the installer command. Invoke it with `$one-thing-at-a-time`.

## License

[MIT](LICENSE)
