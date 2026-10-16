---
name: writing-beamer-generation
description: "Create or revise Quarto Beamer presentations for academic talks, lectures, defenses, and conference papers using a coherent visual and argumentative progression. Use when Codex must convert research materials into slides, structure a timed presentation, or standardize an existing Beamer deck."
---

# Skill: Beamer Generation

# Estilo de presentaciones Beamer con Quarto

## Formato general

Las presentaciones usan Quarto con output Beamer (PDF). El YAML base es:

```yaml
format:
  beamer:
    pdf-engine: xelatex
    theme: "Madrid"
    colortheme: "dolphin"
    fontsize: 10pt
    toc: false
    number-sections: false
    slide-level: 2
    include-in-header: "templates/beamer-progression.tex"
execute:
  echo: false
  warning: false
  message: false
```

## Progresión visual en listas

Las listas de contenido usan progresión visual donde:
- El **item actual** se muestra en texto **normal**
- Los **items por venir** se muestran en **gris transparente**
- Los **items ya discutidos** vuelven a texto **normal**

### Cómo implementar la progresión

Usar el entorno `progresslist` (para itemize) o `progressenum` (para enumerate):

```latex
\begin{progresslist}
  \item Primer punto
  \item Segundo punto
  \item Tercer punto
\end{progresslist}
```

Para control manual del overlay, usar `\pitem{número}{texto}`:

```latex
\begin{itemize}
  \pitem{1}{Primer punto}
  \pitem{2}{Segundo punto}
  \pitem{3}{Tercer punto}
\end{itemize}
```

## Convenciones de diapositivas

- **Slide de sección**: Usar `# Título` (heading nivel 1) o manualmente:
  ```
  ##
  \centering
  \huge
  Título de la sección
  ```

- **Slide de contenido**: Usar `## Título` (heading nivel 2)

- **Figuras**: Usar entorno LaTeX `\begin{figure}` con `\includegraphics`

- **Tablas**: Usar entorno LaTeX `\begin{table}` con `booktabs`

- **Fórmulas inline**: Usar `$...$`

- **Flechas**: Usar `$\rightarrow$`

- **Fuentes de datos**: Incluir como `\caption*{\tiny{\hfill SOURCE: ...}}`

## Estructura típica de una diapositiva de contenido

```
## Título del tema

\begin{progresslist}
  \item Punto principal uno
    \begin{itemize}
      \item Detalle o subpunto
    \end{itemize}
  \item Punto principal dos
  \item Punto principal tres
\end{progresslist}
```

## Idioma

El contenido de las presentaciones puede estar en **español** o en **inglés**, según indique el usuario. Los nombres de figuras, labels y comentarios en código pueden estar en cualquiera de los dos idiomas.
