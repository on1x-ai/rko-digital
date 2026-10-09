# RKO.digital — расчётные счета для digital‑предпринимателей

Сайт‑подборщик банков для IT‑специалистов, фрилансеров, стартапов, онлайн‑школ и e‑commerce. Партнёрские программы банков + будущая реклама на сайте.

## 🚀 Технический стек

- **Astro** (v6) — статический генератор
- **TypeScript** — строгая типизация
- **Tailwind CSS** — утилитарные стили
- **Vercel / Cloudflare Pages** — деплой

## 📁 Структура проекта

```
src/
├── components/          # Astro‑компоненты (AdBlock, BankCard, CTAButton и др.)
├── layouts/            # Базовый макет (BaseLayout.astro)
├── pages/              # Страницы (index.astro, blog/, policy/)
├── content/            # Коллекция статей (blog/*.md)
├── data/               # JSON‑данные (banks.json, niches.json)
└── styles/             # Глобальные стили (global.css)
```

## 🧞 Команды

```bash
npm install          # установка зависимостей
npm run dev          # запуск dev‑сервера на localhost:4321
npm run build        # сборка статического сайта в dist/
npm run preview      # предпросмотр собранного сайта
npm run lint         # проверка кода (если настроено)
```

## 🌐 Деплой

### Vercel

1. Создайте аккаунт на [vercel.com](https://vercel.com)
2. Подключите репозиторий GitHub / GitLab
3. Настройки автоматически определяются (Astro)
4. Добавьте переменные окружения в панели Vercel:
   - `PUBLIC_YANDEX_METRIKA_ID` (опционально)
   - `PUBLIC_GOOGLE_ANALYTICS_ID` (опционально)
5. Деплой запустится автоматически после push в ветку `main`

### Cloudflare Pages

1. В панели Cloudflare Pages создайте новый проект
2. Укажите репозиторий
3. Настройки сборки:
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
4. Добавьте переменные окружения (Environment Variables)
5. Нажмите **Deploy**

## 🔧 Конфигурация

- `astro.config.mjs` — настройки Astro, интеграции (sitemap, robots.txt)
- `src/content.config.ts` — схема коллекции статей
- `tsconfig.json` — алиас `@/*` → `src/*`
- `.env.example` — пример переменных окружения

## 📝 Контент‑коллекция

Статьи хранятся в `src/content/blog/*.md` с фронтмэттером:

```yaml
---
title: 'Заголовок'
description: 'Описание'
pubDate: 2026-01-15
author: 'Автор'
niche: 'it-specialisty'  # один из предопределённых ниш
image: '/og-image.png'   # опционально
---
```

## 📊 SEO и аналитика

- **OG‑теги / Twitter Cards** — настроены в BaseLayout.astro
- **JSON‑LD** — Organization, FAQPage, Article (для статей)
- **Яндекс.Метрика / Google Analytics** — подключаются через переменные окружения
- **Sitemap.xml / robots.txt** — генерируются автоматически

## 🧪 Тестирование

1. **Мобильная адаптация** — проверьте на ширине 390px
2. **Lighthouse** — Performance ≥ 95 (после оптимизации)
3. **Типы** — `npm run typecheck` (если настроено)
4. **Сборка** — `npm run build` должна проходить без ошибок

## 📄 Лицензия

Проприетарный код. Использование только с разрешения правообладателя.

---

*Проект создан для партнёрских программ банков и монетизации через рекламу. Все партнёрские ссылки используют `rel="nofollow sponsored noopener"`.*