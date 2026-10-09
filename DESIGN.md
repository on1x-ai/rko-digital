# DESIGN.md – Дизайн‑система проекта RKO.digital

## 1. Запретный список (ANTI‑LIST)
| Нельзя | Почему |
|---|---|
| Градиент на фоне, форме, карточке, кнопке | Закрывает пустоту, дешёвый способ заполнить место |
| Мелкий капс с разрядкой (LIVE GRAPH, SENSOR SYNC) | Маркер ИИ‑генерации, сразу узнаётся |
| Точка‑разделитель в мете (1 месяц • в наличии) | Тот же маркер, штамп ИИ |
| Дефолтный shadcn без кастомизации | Выглядит как половина проектов на рынке |
| Стекло (blur) на карточках без контента под ним | Дорогой способ нарисовать серый прямоугольник |
| Текст без работы: слоганы, манифесты, описания под карточками | Убираешь — ничего не сломалось, значит лишний |
| Inter, Roboto, Arial, Open Sans, Helvetica | Дефолтные шрифты → похуизм к дизайну |
| Больше двух шрифтовых семей | Третья – шум |
| Больше одного акцентного цвета на экран | Залитый акцентом выглядит дешево |
| Blur на карточках без контента | Перерасход FPS |
| Три колонки KPI на мобильном | Не читается на 390 px |
| Баланс на главном экране | Не работает для агрегатора |
| Фиолетовая палитра | Дефолт всех AI‑сгенерированных сайтов |

---

## 2. CSS‑переменные (variables.css) – подключаются в `src/styles/global.css`
```css
:root {
  /* Фон и поверхности */
  --bg-base: #0A0A0B;
  --bg-surface: #141416;
  --bg-hover: #1C1C1F;
  --bg-elevated: #1F1F23;

  /* Границы */
  --border-subtle: #26262A;
  --border-strong: #35353A;

  /* Текст */
  --text-primary: #F5F5F7;
  --text-secondary: #8A8A8E;
  --text-muted: #5A5A5E;
  --text-inverse: #0A0A0B;

  /* Акценты */
  --accent-primary: #C8FF3D;
  --accent-hover: #B8EF2D;
  --success: #3DD68C;
  --error: #FF4D4D;
  --warning: #FFB84D;

  /* Шрифты */
  --font-display: 'Unbounded', sans-serif; /* заголовки */
  --font-text: 'Golos Text', sans-serif;   /* основной текст */
  --font-mono: 'IBM Plex Mono', monospace;/* цифры и коды */

  /* Радиусы */
  --radius-card: 24px;
  --radius-button: 12px;
  --radius-input: 8px;
  --radius-pill: 9999px;

  /* Отступы (базовая единица 4 px) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  --space-24: 96px;
}
```

---

## 3. Типографика
| Роль | Шрифт | Размер (desktop) | Размер (mobile) | Вес | line‑height |
|---|---|---|---|---|---|
| H1 | Unbounded | 64 px | 36 px | 700 | 1.05 |
| H2 | Unbounded | 40 px | 28 px | 700 | 1.10 |
| H3 | Unbounded | 28 px | 22 px | 600 | 1.20 |
| H4 | Golos Text | 20 px | 18 px | 600 | 1.30 |
| Body | Golos Text | 16 px | 15 px | 400 | 1.60 |
| Body small | Golos Text | 14 px | 13 px | 400 | 1.50 |
| Caption | Golos Text | 12 px | 12 px | 500 | 1.40 |
| Metric number | Unbounded | 32 px | 24 px | 700 | 1.00 |
| Metric label | Golos Text | 12 px | 12 px | 500 | 1.40 |
| Code / status | IBM Plex Mono | 13 px | 12 px | 400 | 1.40 |

**Правила**
- Максимум 2 семейства шрифтов (Unbounded + Golos Text). IBM Plex Mono только для цифр/кода.
- Числа в UI – `font-variant-numeric: tabular-nums;`.
- Не использовать мелкий caps с разрядкой.

---

## 4. Сетка
- **Контейнер**: `max-width: 1200px; margin: 0 auto;`
- **Колонки**: 12‑col на десктопе, 6‑col на планшете, 4‑col на мобильных.
- **Gutter**: 24 px десктоп, 16 px мобильные.
- **Отступы от краёв**: 48 px (tablet), 24 px (mobile), 0 px (центр на десктоп).
- **Радиусы** задаются переменной `--radius-card` (super‑ellipse через `border-radius`).
- **Тени запрещены** – используем только границы (`border` с переменными).

---

## 5. Анатомия карточки банка (BankCard)
```
┌─────────────────────────────────────────┐
│ [logo 32x32]  Т‑Банк                    │
│               Для IT‑фрилансеров       │
│                                         │
│  ───────────────────────────────────── │
│                                         │
│  Открытие   Обслуживание   Валюта      │
│  1 день      0 ₽/490 ₽      SWIFT      │
│                                         │
│  ───────────────────────────────────── │
│                                         │
│  • Бесплатное открытие                  │
│  • Валютный контроль                    │
│  • Эквайринг                            │
│                                         │
│  [Открыть счёт →]                       │
│  [Выбор редакции]                       │
└─────────────────────────────────────────┘
```
**Состояния**
- **Default** – `background: var(--bg-surface); border: 1px solid var(--border-subtle);`
- **Hover** – `background: var(--bg-hover); border-color: var(--border-strong);`
- **Featured** – акцентная кнопка `background: var(--accent-primary); color: var(--text-inverse);`

---

## 6. Анатомия метрик (Metric)
```html
<div class="flex flex-col items-center">
  <span class="font-display text-2xl font-bold tabular-nums text-primary">32 864</span>
  <span class="font-text text-sm text-secondary">Транзакций в месяц</span>
</div>
```
- Число – `Unbounded`, `font-weight: 700`, `tabular-nums`.
- Подпись – `Golos Text`, `12 px`, `--text-secondary`.
- Разделитель – тонкая линия `1px solid var(--border-subtle)`, **не** точка.

---

## 7. Пустые состояния (EmptyState)
- **Иллюстрация** (svg/png) слева или сверху.
- **Заголовок** – крупный H3, смысловой.
- **Описание** – короткое, полезное.
- **CTA** – главная кнопка `CTAButton`.
- **Не** центрировать серым текстом без визуального контекста.

---

## 8. Кнопки (CTAButton)
| Variant | Background | Text | Border | Когда использовать |
|---|---|---|---|---|
| Primary | `var(--accent-primary)` | `var(--text-inverse)` | none | Главное действие на странице |
| Secondary | transparent | `var(--text-primary)` | `1px solid var(--border-subtle)` | Второстепенное действие |
| Ghost | transparent | `var(--text-secondary)` | none | Навигация, отмена |
| Link | none | `var(--accent-primary)` | none | Inline‑ссылка |

**Размеры** – `sm` (32 px), `md` (40 px), `lg` (48 px). Padding ≈ `12‑20‑16‑24‑20‑28`.

---

## 9. Формы
- Поле: `background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-input); padding: 12px 16px;`
- `:focus` → `border-color: var(--accent-primary); outline: none;`
- Ошибка → `border-color: var(--error); color: var(--error);`, сообщение под полем.
- Метка – `font-text 14 px var(--text-secondary)` над полем.

---

## 10. Ссылки партнёров (PartnerLink)
```html
<a href="https://example.com/partner/tbank" rel="nofollow sponsored noopener" target="_blank" data-erid="" class="text-accent-primary underline">Открыть счёт в Т‑Банке</a>
```
- `rel="nofollow sponsored noopener"` обязателен.
- `data-erid` – placeholder для рекламных сетей.

---

## 11. FAQ (аккордеон) + Schema.org
- Структура: массив `{question, answer}`.
- При раскрытии анимация плавного высоты.
- Вставляем JSON‑LD `FAQPage` в `<script type="application/ld+json">`.

---

## 12. Review
- Цитата в кавычках, фон `var(--bg-surface)`, граница `var(--border-subtle)`. 
- Текст – `font-text`, автор/бизнес – `font-text text-muted`.

---

## 13. AdBlock (заглушка)
```html
<!-- AD BLOCK: banner (970x90) -->
<div class="h-24 w-full bg-neutral-900 flex items-center justify-center text-muted">[Banner Ad]</div>
```
- Разные типы: `banner`, `inline`, `sidebar` – только контейнер с комментарием.

---

## 14. Ссылки на референсы (moodboard)
Мудборд хранится в `design/moodboard/`:
- `ref-01-bento.txt` – Bento‑сетка, **берём** композицию, **не берём** градиенты. 
- `ref-02-dark-fintech.txt` – Тёмная тема, **берём** глубокий чёрный фон, **не берём** blur, фиолет. 
- `ref-03-typography.txt` – Расставление типографики, **берём** крупные заголовки, **не берём** мелкий caps. 
- `ref-04-mobile.txt` – Мобильные карточки, **берём** читаемость 390 px, **не берём** 3‑колонки KPI. 
- `ref-05-shadcn.txt` – Паттерны shadcn/ui, **берём** структуру, **не берём** дефолтные радиусы/цвета.

---

## 15. Общие правила UI
- **Не** использовать градиенты, blur, точку‑разделитель, более 2 шрифтов.
- **Только** один акцентный цвет `#C8FF3D` на экране.
- **Все** цифры – `tabular-nums`.
- **Микроскопический** контент сначала убираем – если удаляется без поломки, удаляем.
- **Мобильная** вёрстка проверяется на ширине 390 px.
- **Тени** запрещены – заменяем границами.
- **Локализация** – русский язык, `lang="ru"` в `<html>`.

---

## 16. Дальнейшие шаги проекта
1. **Создать moodboard** – 5 txt‑файлов в `design/moodboard/` (см. раздел 14). 
2. **Подключить скиллы** в указанном порядке (UX → анти‑шаблон → минимализм → high‑end → shadcn). 
3. **Инициализировать shadcn MCP** (`npx shadcn@latest mcp init --client claude`). 
4. **Разработать компоненты** согласно спеке (CTAButton, PartnerLink, FAQ, Review, BankCard, BankComparison, StepGuide, AdBlock, RelatedArticles, Metric, EmptyState). 
5. **Собрать страницы** (главная, нишевые, блог, статья, политика). 
6. **Настроить SEO** (astro‑seo, sitemap, robots, Schema.org). 
7. **Подключить аналитику** (Yandex.Metrika, Google Analytics через .env). 
8. **Тестировать** на Lighthouse (> 95 Performance) и мобильных устройствах. 
9. **Деплой** на Vercel/Cloudflare Pages (site‑placeholder в `astro.config.mjs`).

---

### Файловая структура (частичный фрагмент)
```
design/
  moodboard/
    ref-01-bento.txt
    ref-02-dark-fintech.txt
    ref-03-typography.txt
    ref-04-mobile.txt
    ref-05-shadcn.txt
DESIGN.md
```

*Следующим шагом – **Шаг 2**: создать moodboard‑txt‑файлы.*