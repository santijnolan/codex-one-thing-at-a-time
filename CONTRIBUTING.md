# Contributing

Gracias por mejorar `one-thing-at-a-time`.

## Antes de abrir un PR

1. Creá un fork y una rama descriptiva.
2. Modificá la skill dentro de `skills/one-thing-at-a-time/`.
3. Conservá el contrato principal: una decisión por vez durante la planificación; ejecución completa después de cerrar el plan.
4. Mantené `SKILL.md` conciso, genérico y libre de datos, rutas o proyectos privados.
5. Ejecutá:

```bash
python3 -m pip install PyYAML
python3 scripts/validate_skill.py
```

## En el PR

Explicá:

- qué comportamiento cambia;
- por qué mejora la experiencia;
- un ejemplo de antes y después;
- cómo lo validaste.

Los cambios deben mantener sincronizados `SKILL.md` y `agents/openai.yaml`.
