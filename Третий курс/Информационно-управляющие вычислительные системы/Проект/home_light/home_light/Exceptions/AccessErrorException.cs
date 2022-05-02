namespace home_light.Exceptions
{
    /// <summary>
    /// Access Error Exception
    /// </summary>
    [Serializable]
    public class AccessErrorException : Exception
    {
        /// <summary>
        /// Базовый конструктор
        /// </summary>
        public AccessErrorException() : base() { }
        /// <summary>
        /// Базовый конструктор с описанием сообщения
        /// </summary>
        /// <param name="message"></param>
        public AccessErrorException(string message) : base(message) { }
    }
}
