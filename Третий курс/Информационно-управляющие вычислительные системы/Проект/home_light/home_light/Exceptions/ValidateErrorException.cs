namespace home_light.Exceptions
{
    /// <summary>
    /// Validate Error Exception
    /// </summary>
    [Serializable]
    public class ValidateErrorException : Exception
    {
        /// <summary>
        /// Базовый конструктор
        /// </summary>
        public ValidateErrorException() : base() { }
        /// <summary>
        /// Базовый конструктор с описанием сообщения
        /// </summary>
        /// <param name="message"></param>
        public ValidateErrorException(string message) : base(message) { }
    }
}
