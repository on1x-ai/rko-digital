/**
 * Вычисляет примерное время чтения статьи
 * @param text Текст статьи
 * @returns Время чтения в минутах (округляется вверх)
 */
export function readingTime(text: string): number {
  // Убираем HTML-теги, Markdown синтаксис
  const cleanText = text
    .replace(/<[^>]+>/g, ' ') // HTML теги
    .replace(/[#*`\[\]()!]/g, ' ') // Markdown синтаксис
    .replace(/\s+/g, ' ') // Множественные пробелы
    .trim();

  // Считаем слова (разделители: пробелы, переносы строк)
  const wordCount = cleanText.split(/\s+/).filter(word => word.length > 0).length;
  
  // Средняя скорость чтения: 200 слов/минуту
  const minutes = wordCount / 200;
  
  // Округляем вверх, минимум 1 минута
  return Math.max(1, Math.ceil(minutes));
}