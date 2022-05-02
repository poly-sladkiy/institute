namespace home_light.Exceptions
{
    /// <summary>
    /// Simple GraphQL Validate Exception
    /// </summary>
    [Serializable]
    public class GraphQLValidateException : Exception
    {
        /// <summary>
        /// Base
        /// </summary>
        public GraphQLValidateException() : base() { }
        /// <summary>
        /// Exeption with desctiption message
        /// </summary>
        /// <param name="message"></param>
        public GraphQLValidateException(string message) : base(message) { }
    }
}
