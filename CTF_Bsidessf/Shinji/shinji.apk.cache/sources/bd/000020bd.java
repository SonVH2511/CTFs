package androidx.core.app;

import android.content.Context;
import android.util.Log;
import android.util.Xml;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import org.xmlpull.v1.XmlSerializer;

/* loaded from: classes.dex */
public class AppLocalesStorageHelper {
    static final String APPLICATION_LOCALES_RECORD_FILE = "androidx.appcompat.app.AppCompatDelegate.application_locales_record_file";
    static final boolean DEBUG = false;
    static final String LOCALE_RECORD_ATTRIBUTE_TAG = "application_locales";
    static final String LOCALE_RECORD_FILE_TAG = "locales";
    static final String TAG = "AppLocalesStorageHelper";
    private static final Object sAppLocaleStorageSync = new Object();

    private AppLocalesStorageHelper() {
    }

    /* JADX WARN: Code restructure failed: missing block: B:20:0x0044, code lost:
        r1 = r3.getAttributeValue(null, androidx.core.app.AppLocalesStorageHelper.LOCALE_RECORD_ATTRIBUTE_TAG);
     */
    /*
        Code decompiled incorrectly, please refer to instructions dump.
        To view partially-correct code enable 'Show inconsistent code' option in preferences
    */
    public static java.lang.String readLocales(android.content.Context r9) {
        /*
            java.lang.Object r0 = androidx.core.app.AppLocalesStorageHelper.sAppLocaleStorageSync
            monitor-enter(r0)
            java.lang.String r1 = ""
            java.lang.String r2 = "androidx.appcompat.app.AppCompatDelegate.application_locales_record_file"
            java.io.FileInputStream r2 = r9.openFileInput(r2)     // Catch: java.io.FileNotFoundException -> L79 java.lang.Throwable -> L7c
            org.xmlpull.v1.XmlPullParser r3 = android.util.Xml.newPullParser()     // Catch: java.lang.Throwable -> L4f java.io.IOException -> L51 org.xmlpull.v1.XmlPullParserException -> L53
            java.lang.String r4 = "UTF-8"
            r3.setInput(r2, r4)     // Catch: java.lang.Throwable -> L4f java.io.IOException -> L51 org.xmlpull.v1.XmlPullParserException -> L53
            int r4 = r3.getDepth()     // Catch: java.lang.Throwable -> L4f java.io.IOException -> L51 org.xmlpull.v1.XmlPullParserException -> L53
        L19:
            int r5 = r3.next()     // Catch: java.lang.Throwable -> L4f java.io.IOException -> L51 org.xmlpull.v1.XmlPullParserException -> L53
            r6 = r5
            r7 = 1
            if (r5 == r7) goto L47
            r5 = 3
            if (r6 != r5) goto L2a
            int r7 = r3.getDepth()     // Catch: java.lang.Throwable -> L4f java.io.IOException -> L51 org.xmlpull.v1.XmlPullParserException -> L53
            if (r7 <= r4) goto L47
        L2a:
            if (r6 == r5) goto L19
            r5 = 4
            if (r6 != r5) goto L30
            goto L19
        L30:
            java.lang.String r5 = r3.getName()     // Catch: java.lang.Throwable -> L4f java.io.IOException -> L51 org.xmlpull.v1.XmlPullParserException -> L53
            java.lang.String r7 = "locales"
            boolean r7 = r5.equals(r7)     // Catch: java.lang.Throwable -> L4f java.io.IOException -> L51 org.xmlpull.v1.XmlPullParserException -> L53
            if (r7 == 0) goto L46
            java.lang.String r7 = "application_locales"
            r8 = 0
            java.lang.String r7 = r3.getAttributeValue(r8, r7)     // Catch: java.lang.Throwable -> L4f java.io.IOException -> L51 org.xmlpull.v1.XmlPullParserException -> L53
            r1 = r7
            goto L47
        L46:
            goto L19
        L47:
            if (r2 == 0) goto L62
            r2.close()     // Catch: java.io.IOException -> L4d java.lang.Throwable -> L7c
        L4c:
            goto L62
        L4d:
            r3 = move-exception
            goto L4c
        L4f:
            r3 = move-exception
            goto L70
        L51:
            r3 = move-exception
            goto L54
        L53:
            r3 = move-exception
        L54:
            java.lang.String r4 = "AppLocalesStorageHelper"
            java.lang.String r5 = "Reading app Locales : Unable to parse through file :androidx.appcompat.app.AppCompatDelegate.application_locales_record_file"
            android.util.Log.w(r4, r5)     // Catch: java.lang.Throwable -> L4f
            if (r2 == 0) goto L62
            r2.close()     // Catch: java.io.IOException -> L4d java.lang.Throwable -> L7c
            goto L4c
        L62:
            boolean r3 = r1.isEmpty()     // Catch: java.lang.Throwable -> L7c
            if (r3 != 0) goto L69
            goto L6e
        L69:
            java.lang.String r3 = "androidx.appcompat.app.AppCompatDelegate.application_locales_record_file"
            r9.deleteFile(r3)     // Catch: java.lang.Throwable -> L7c
        L6e:
            monitor-exit(r0)     // Catch: java.lang.Throwable -> L7c
            return r1
        L70:
            if (r2 == 0) goto L77
            r2.close()     // Catch: java.io.IOException -> L76 java.lang.Throwable -> L7c
            goto L77
        L76:
            r4 = move-exception
        L77:
            throw r3     // Catch: java.lang.Throwable -> L7c
        L79:
            r2 = move-exception
            monitor-exit(r0)     // Catch: java.lang.Throwable -> L7c
            return r1
        L7c:
            r1 = move-exception
            monitor-exit(r0)     // Catch: java.lang.Throwable -> L7c
            throw r1
        */
        throw new UnsupportedOperationException("Method not decompiled: androidx.core.app.AppLocalesStorageHelper.readLocales(android.content.Context):java.lang.String");
    }

    public static void persistLocales(Context context, String locales) {
        synchronized (sAppLocaleStorageSync) {
            if (locales.equals("")) {
                context.deleteFile(APPLICATION_LOCALES_RECORD_FILE);
                return;
            }
            try {
                FileOutputStream fos = context.openFileOutput(APPLICATION_LOCALES_RECORD_FILE, 0);
                XmlSerializer serializer = Xml.newSerializer();
                try {
                    try {
                        serializer.setOutput(fos, null);
                        serializer.startDocument("UTF-8", true);
                        serializer.startTag(null, LOCALE_RECORD_FILE_TAG);
                        serializer.attribute(null, LOCALE_RECORD_ATTRIBUTE_TAG, locales);
                        serializer.endTag(null, LOCALE_RECORD_FILE_TAG);
                        serializer.endDocument();
                    } catch (Exception e) {
                        Log.w(TAG, "Storing App Locales : Failed to persist app-locales in storage ", e);
                        if (fos != null) {
                            fos.close();
                        }
                    }
                    if (fos != null) {
                        fos.close();
                    }
                } catch (IOException e2) {
                }
            } catch (FileNotFoundException e3) {
                Log.w(TAG, String.format("Storing App Locales : FileNotFoundException: Cannot open file %s for writing ", APPLICATION_LOCALES_RECORD_FILE));
            }
        }
    }
}