/**
 * Вычисляет примерное время чтения статьи
 * @param text Текст статьи
 * @param slug Опциональный slug статьи для фиксированных значений
 * @returns Время чтения в минутах
 */
export function readingTime(text: string, slug?: string): number {
  // Фиксированные значения для конкретных статей по требованию
  const fixedTimes: Record<string, number> = {
    'npd-vs-ip': 8,
    'rko-dlya-startapa': 9,
    'rko-dlya-online-shkoly': 8,
    'valyutnyj-kontrol-dlya-it': 8,
    'kakoj-okved-vybrat-dlya-lgotnoj-usn-3': 7,
    'kak-vybrat-bank-dlya-it-frilansera': 7,
  };

  // Если slug указан и есть фиксированное значение - возвращаем его
  if (slug && fixedTimes[slug]) {
    return fixedTimes[slug];
  }

  // Иначе считаем автоматически
  // Убираем HTML-теги, Markdown синтаксис, компоненты
  const cleanText = text
    .replace(/<[^>]+>/g, ' ') // HTML теги
    .replace(/[#*`\[\]()!]/g, ' ') // Markdown синтаксис
    .replace(/<[A-Za-z][^>]*\/>/g, ' ') // Самозакрывающиеся компоненты
    .replace(/<[A-Za-z][^>]*>.*?<\/[A-Za-z][^>]*>/gs, ' ') // Компоненты с содержимым
    .replace(/\s+/g, ' ') // Множественные пробелы
    .trim();

  // Считаем символы без пробелов (более точный метод)
  const charCount = cleanText.replace(/\s/g, '').length;
  
  // Средняя скорость чтения: 1000 символов без пробелов в минуту
  // Это соответствует примерно 200-230 словам в минуту
  const minutes = charCount / 1000;
  
  // Округляем до десятых, минимум 1 минута
  const rounded = Math.max(1, Math.round(minutes * 10) / 10);
  
  return rounded;
}

/**
 * Форматирует время чтения для отображения
 * @param minutes Количество минут
 * @returns Форматированная строка (например "1 мин", "7-9 мин")
 */
export function formatReadingTime(minutes: number): string {
  if (minutes >= 6) {
    // Для статей от 6 минут показываем диапазон ±1 минута
    const min = Math.floor(minutes - 1);
    const max = Math.ceil(minutes + 1);
    return `${min}–${max} мин`;
  } else if (minutes >= 5) {
    // Для 5 минут показываем "5-6 мин"
    return "5-6 мин";
  }
  
  // Для коротких статей округляем до целого
  const rounded = Math.round(minutes);
  return `${rounded} мин`;
}