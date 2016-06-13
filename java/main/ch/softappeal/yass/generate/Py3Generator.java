package ch.softappeal.yass.generate;

import ch.softappeal.yass.serialize.fast.BaseTypeHandler;
import ch.softappeal.yass.serialize.fast.BaseTypeHandlers;
import ch.softappeal.yass.serialize.fast.TypeDesc;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

/**
 * You must use the "-parameters" option for javac to get the real method parameter names.
 */
public final class Py3Generator {

    public static final TypeDesc BOOLEAN_DESC = new TypeDesc(TypeDesc.FIRST_ID, BaseTypeHandlers.BOOLEAN);
    public static final TypeDesc DOUBLE_DESC = new TypeDesc(TypeDesc.FIRST_ID + 1, BaseTypeHandlers.DOUBLE);
    public static final TypeDesc STRING_DESC = new TypeDesc(TypeDesc.FIRST_ID + 2, BaseTypeHandlers.STRING);
    public static final TypeDesc BYTES_DESC = new TypeDesc(TypeDesc.FIRST_ID + 3, BaseTypeHandlers.BYTE_ARRAY);
    public static final TypeDesc BIGINTEGER_DESC = new TypeDesc(TypeDesc.FIRST_ID + 4, BaseTypeHandlers.BIGINTEGER);
    public static final int FIRST_DESC_ID = TypeDesc.FIRST_ID + 5;

    public static List<BaseTypeHandler<?>> baseTypeHandlers(final BaseTypeHandler<?>... handlers) {
        final List<BaseTypeHandler<?>> h = new ArrayList<>();
        h.add((BaseTypeHandler<?>)BOOLEAN_DESC.handler);
        h.add((BaseTypeHandler<?>)DOUBLE_DESC.handler);
        h.add((BaseTypeHandler<?>)STRING_DESC.handler);
        h.add((BaseTypeHandler<?>)BYTES_DESC.handler);
        h.add((BaseTypeHandler<?>)BIGINTEGER_DESC.handler);
        h.addAll(Arrays.asList(handlers));
        return h;
    }

    public static Collection<TypeDesc> baseTypeDescs(final TypeDesc... descs) {
        final List<TypeDesc> d = new ArrayList<>();
        d.add(BOOLEAN_DESC);
        d.add(DOUBLE_DESC);
        d.add(STRING_DESC);
        d.add(BYTES_DESC);
        d.add(BIGINTEGER_DESC);
        d.addAll(Arrays.asList(descs));
        return d;
    }

    // todo: implement

}
