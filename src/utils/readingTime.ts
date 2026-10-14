/**
 * Вычисляет примерное время чтения статьи
 * @param text Текст статьи
 * @returns Время чтения в минутах (точный расчёт по символам без пробелов)
 */
export function readingTime(text: string): number {
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
  
  // Если больше 5 минут, показываем диапазон ±1 минута
  if (rounded >= 5) {
    // Возвращаем среднее значение для использования в вычислениях
    return rounded;
  }
  
  return rounded;
}

/**
 * Форматирует время чтения для отображения
 * @param minutes Количество минут
 * @returns Форматированная строка (например "1 мин", "6-8 мин")
 */
export function formatReadingTime(minutes: number): string {
  if (minutes >= 5) {
    // Для длинных статей показываем диапазон
    const min = Math.floor(minutes - 1);
    const max = Math.ceil(minutes + 1);
    return `${min}–${max} мин`;
  }
  
  // Для коротких статей округляем до целого
  const rounded = Math.round(minutes);
  return `${rounded} мин`;
}